# Sus Cartoon Factory 🎬

Automated, zero-paid-API **original 2D preschool cartoon generator**.

This project draws its own simple characters and backgrounds, narrates with eSpeak NG, composes a procedural instrumental soundtrack, and exports an MP4 + thumbnail + metadata. It can run entirely in GitHub Actions from a phone.

## Run on your phone
1. Open **Actions → Generate original cartoon**.
2. Tap **Run workflow** and choose **random**, **colors**, **counting**, or **shapes**.
3. Open the completed workflow run and download the **cartoon-...** artifact containing an MP4 and thumbnail.
4. Automatic runs are scheduled Tuesdays and Fridays (GitHub may delay scheduled runs).

## Optional YouTube uploads
The workflow can automatically **upload PRIVATE Made for Kids** videos using the YouTube Data API once you set 3 Actions secrets in **Settings → Secrets and variables → Actions**:

* `YT_CLIENT_ID`
* `YT_CLIENT_SECRET`
* `YT_REFRESH_TOKEN`

Obtain these from a Google Cloud project with YouTube Data API v3 enabled and an OAuth consent flow for `https://www.googleapis.com/auth/youtube.upload`. **Never put credentials in a repository or share them in chat.** This project does not publish publicly without review.

## What this is and isn't
- ✅ Real Python animation and rendering, narrated educational scripts, original synthetic music, automatic thumbnail, planned workflow
- ✅ Runs on standard GitHub-hosted Ubuntu runners in a public repo (subject to GitHub usage policy/limits)
- ❌ No generative AI songs or Pixar/Cocomelon-grade 3D graphics
- ❌ No automatic public posting or guaranteed monetization

These stories are **template-generated**, repetitive if published in bulk, and have a robotic voice. Children's content requires careful human review and accurate **Made for Kids** setting. YouTube may refuse monetization of mass-produced content. Avoid copying copyrighted Cocomelon characters, sounds, or artwork.

Local run: `pip install -r requirements.txt`, install system `ffmpeg` and `espeak-ng`, then `python factory.py --topic random --output build`.
