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
  },
  "lego": {
    "dataset": "lego",
    "article": "a",
    "name": "excavator"
  }
}

queries = [
  {
    "name": "blue",
    "query": "{} blue {}"
  },
  {
    "name": "pretzel",
    "query": "{} {} made out of pretzel; food photography; photo-realistic"
  },
  {
    "name": "expressionism",
    "query": "{} expressionist {} painted by Pablo Picasso; expressionism; art photography"
  }
]

for scene in scenes.values():
  for query in queries:
    current_query = query['query'].format(scene["article"], scene["name"]).strip()
    current_query = current_query[:1].upper() + current_query[1:]

    # Render stylized scene
    command = f'python run_nerf_clip.py --expname {scene["dataset"]}_{query["name"]}_comparison --config configs/{scene["dataset"]}.txt --use_clip --w_clip 1.0 --description "{current_query}" --ft_path checkpoints/{scene["dataset"]}.tar --sample_scale 40 --i_print 500 --i_img 10000 --i_weights 10000 --i_testset 10000 --i_video 10000'
    os.system(command)
