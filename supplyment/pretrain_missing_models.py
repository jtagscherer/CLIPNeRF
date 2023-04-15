import os

scenes = {
  "chair": {
    "dataset": "chair",
    "article": "a",
    "name": "chair"
  },
  "hotdog": {
    "dataset": "hotdog",
    "article": "a",
    "name": "hotdog"
  }
}

for scene in scenes.values():
  # Train vanilla NeRF
  command = f'python run_nerf_clip.py --expname {scene["dataset"]}_pretrain --config configs/{scene["dataset"]}.txt --sample_scale 40 --i_print 5000 --i_img 5000 --i_weights 5000 --i_testset 5000 --i_video 5000'
  os.system(command)
