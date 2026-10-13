#!/usr/bin/env python3
"""Deterministically create a shard of a 10- or 100-Short batch.

Each video gets a unique topic in the run. Manifests are updated after every
video, so interrupted runs still leave useful diagnostic information.
"""
import argparse
import json
import os
from pathlib import Path
import random
import shutil
import sys
import traceback
from argparse import Namespace

from factory import TOPICS, generate


def plan_topics(total, run_seed):
    if total not in (10, 100):
        raise ValueError("Batch size must be 10 or 100")
    if total > len(TOPICS):
        raise ValueError("Not enough unique topics to create this batch")
    available = list(TOPICS)
    random.Random(run_seed).shuffle(available)
    return available[:total]


def write_manifest(folder, rows, total, shard):
    payload = {
        "requested_batch_size": total,
        "shard": shard,
        "completed": sum(1 for row in rows if row["status"] == "generated"),
        "failed": sum(1 for row in rows if row["status"] == "failed"),
        "videos": rows,
    }
    (folder / "manifest.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, choices=(10, 100), required=True)
    parser.add_argument("--shard", type=int, required=True)
    parser.add_argument("--shard-size", type=int, default=10)
    parser.add_argument("--run-seed", type=int,
                        default=int(os.environ.get("GITHUB_RUN_ID", "20261013")))
    parser.add_argument("--output", default="batch-shorts")
    parser.add_argument("--fps", type=int, default=10)
    args = parser.parse_args(argv)

    selected = plan_topics(args.count, args.run_seed)
    start = args.shard * args.shard_size
    end = min(start + args.shard_size, args.count)
    if not (0 <= start < args.count) or args.shard_size <= 0:
        parser.error("shard number or size is out of range")

    root = Path(args.output)
    root.mkdir(parents=True, exist_ok=True)
    records = []
    for index in range(start, end):
        topic = selected[index]
        episode = index + 1
        folder = root / f"short-{episode:03d}"
        print(f"Generating {episode}/{args.count}: {topic}", flush=True)
        try:
            meta = generate(Namespace(
                topic=topic, seed=args.run_seed * 1000 + episode,
                output=str(folder), fps=args.fps, format="shorts", no_voice=False
            ))
            video = folder / "episode.mp4"
            if video.stat().st_size <= 100_000:
                raise RuntimeError(f"Video missing or too small: {video}")
            if meta["video_format"] != "shorts" or meta["duration_seconds"] >= 180:
                raise RuntimeError(f"Invalid Shorts metadata: {video}")
            records.append({
                "episode": episode, "topic": topic, "status": "generated",
                "duration_seconds": meta["duration_seconds"],
                "video": str(video)
            })
        except Exception as exc:
            traceback.print_exc()
            records.append({
                "episode": episode, "topic": topic, "status": "failed",
                "error": f"{type(exc).__name__}: {exc}"[:800]
            })
        finally:
            # Keep MP4, metadata, subtitles and thumbnail, not bulky intermediates.
            shutil.rmtree(folder / "speech", ignore_errors=True)
            (folder / "audio.wav").unlink(missing_ok=True)
            write_manifest(root, records, args.count, args.shard)

    generated = sum(row["status"] == "generated" for row in records)
    print(f"Shard {args.shard}: generated {generated}/{end-start} videos.", flush=True)
    return 1 if generated != end - start else 0


if __name__ == "__main__":
    sys.exit(main())
