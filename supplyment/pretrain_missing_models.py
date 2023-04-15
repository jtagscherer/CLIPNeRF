import os

scenes = {
  "chair": {
    "dataset": "chair",
    "article": "a",
    "name": "chair"
  },
  "drums": {
    "dataset": "drums",
    "article": "",
    "name": "drums"
  },
  "ficus": {
    "dataset": "ficus",
    "article": "a",
    "name": "ficus plant"
  },
  "hotdog": {
    "dataset": "hotdog",
    "article": "a",
    "name": "hotdog"
  },
  "materials": {
    "dataset": "materials",
    "article": "",
    "name": "spheres"
  },
  "mic": {
    "dataset": "mic",
    "article": "a",
    "name": "microphone"
  },
  "ship": {
    "dataset": "ship",
    "article": "a",
    "name": "ship"
  }
}

for scene in scenes.values():
  # Train vanilla NeRF
  command = f'python run_nerf_clip.py --expname {scene["dataset"]}_pretrain --config configs/{scene["dataset"]}.txt --sample_scale 40 --i_print 5000 --i_img 5000 --i_weights 5000 --i_testset 5000 --i_video 5000'
  os.system(command)
