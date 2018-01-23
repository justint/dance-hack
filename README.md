# Dance Hack
Using [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) motion detection, this repo is a web app that uses a video cam to detect the dancing motions of people and chooses an appropriate song to play using the Spotify API.

This SB Hacks 2018 hackathon project won Best Modern C++ by Toyon Research Corporation!

Developed by [Justin Tennant](https://github.com/justint) & [Travis Cramer](https://github.com/travis-cramer).

_NOTE_: The following files need Spotify variables unique to your Spotify app & account to run:
- `playground.py` (Spotify client_id, client_secret)
- `dancehack/dj/views.py` (Spotify client_id, client_secret, username)
- `dancehack/dj/templates/dj/base.html` (token)
