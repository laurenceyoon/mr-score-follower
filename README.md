# Mixed Reality Score Follower

We propose a real-time music tracking system based on a score following algorithm based on Online Dynamic Time Warping(OLTW) in music performance using a mixed reality device. This system visualizes sheet music synchronized with actual performances to users wearing mixed reality (Hololens2) devices. At the same time, it provides a function of synchronizing each score after classifying and arranging the score by part at the location of the actual instrument in the space.

## Environments
- python3.10
- Unity
- Photon engine

## How to setup

On server-side

```bash
# create conda environment
$ conda env create --file environment.yml
$ conda activate msf

# run the fastapi application
$ uvicorn app.main:app --reload
```

On Dummy-Unity-side
- To be updated

## Related Sources
- Hololens Client: [Source Code](https://github.com/laurenceyoon/mr-score-follower-hololens) developed with MRTK(Mixed Reality Toolkit)
- Demo Video: 
  - [Score following demo in mixed reality](https://youtube.com/playlist?list=PLVMiFGKhAemGDNOlLwyEhtK2AvJTggTWx)
  - [Score(parts) placement in Hololens2](https://youtu.be/CQXPRSl0iqk)
  - [Score Highlighting in Unity](https://youtu.be/ZGVP5SvyoJU)