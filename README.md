# Little Wonder Lab Shorts Factory

Generates 9:16 educational animated Shorts using Python, Pillow, FFmpeg, and a narrated voice. Works from GitHub Actions on a phone, without paid video-generation APIs.

## What can it make?

- **183 lesson topics:** the original 3, another 30, plus **150 additional vocabulary themes** in 15 categories.
- Each new vocabulary theme has **five topic-specific words** and its own introductory and closing script.
- The new themes use **stylized vocabulary cards**, not literal custom illustrations of all 750 words. Existing artwork is template-based.
- Sound: Jenny Neural TTS when available, with an offline eSpeak fallback.

## Make 10 or 100 videos on your phone

1. Open [Actions → Generate 10 or 100 Shorts](https://github.com/aurexvelion/Sus/actions/workflows/ten-shorts.yml).
2. Tap **Run workflow** (switch to desktop site on mobile if needed).
3. Choose **10** or **100** in the `count` selector.
4. Leave **upload_to_youtube** **off** to generate downloadable videos safely. Turn it **on** only if you want to attempt YouTube uploads and understand your channel's current upload limits.
5. Start the run, wait for the jobs to finish, then open the run's **Artifacts** section to download the MP4s.

**100 mode:** ten parallelizable jobs, each with ten non-repeating lesson topics. There are **10 ZIP artifacts**, one per group of ten; the videos are not combined into one giant ZIP. Each ZIP includes rendered videos, thumbnails, captions, metadata, and a manifest. Jobs run with a maximum of two at once to manage resources.

If one video fails, that job still tries to generate the others. Files already generated are saved before any YouTube upload starts. Artifacts are retained for seven days.

**10 mode:** one group of ten distinct topics and one ZIP artifact.

A separate [single-video generator](https://github.com/aurexvelion/Sus/actions/workflows/generate.yml) also exists.

## YouTube uploads and limits

The upload toggle requires GitHub repository OAuth secrets: `YT_CLIENT_ID`, `YT_CLIENT_SECRET`, and `YT_REFRESH_TOKEN`.

Uploads request **Public** visibility and **Made for Kids** audience classification, because the cartoons target young children. YouTube can still restrict visibility or refuse an upload.

**Observed limit:** A prior ten-video run uploaded seven videos, then YouTube rejected the eighth with `uploadLimitExceeded`. Therefore, generating 100 videos does **not** mean your channel can publish 100 videos immediately. Turning on uploads may fail when that account limit is reached. YouTube also places API quotas on uploads.

Review the scripts, accuracy, captions, and images before publishing. Mass-produced repetitive videos may not qualify for YouTube monetization.

## Local use

Install FFmpeg and eSpeak NG, then:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python factory.py --topic random --format shorts --output build
python batch_shorts.py --count 10 --shard 0 --output batch-shorts
# For 100 locally, generate shards 0 through 9 with --count 100.
```

Each MP4 is 720 × 1280 pixels (9:16), H.264 video with AAC audio. The new vocabulary topics are selected in non-repeating order within a batch, based on the GitHub run ID. Repeated runs can reuse topics with different seeds.

GitHub runner time, disk space, YouTube channel limits, and network availability can all affect completion. The batch is not automatically launched by commits.
