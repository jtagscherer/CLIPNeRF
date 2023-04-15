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
  "lego": {
    "dataset": "lego",
    "article": "a",
    "name": "excavator"
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

queries = [
  "{} blue {}",
  "{} {} made out of pretzel; food photography; photo-realistic",
  "{} {} made out of pizza; food photography; photo-realistic",
  "{} pencil sketch {}; Art on Instagram; trending on artstation",
  "{} expressionist {} painted by Pablo Picasso; expressionism; art photography"
]

for scene in scenes.values():
  for query in queries:
    current_query = query.format(scene["article"], scene["name"]).strip()
    current_query = current_query[:1].upper() + current_query[1:]

    # Render stylized scene
    command = f'python run_nerf_clip.py --expname {scene["dataset"]}_comparison --config configs/{scene["dataset"]}.txt --use_clip --w_clip 1.0 --description "{current_query}" --ft_path checkpoints/{scene["dataset"]}.tar --sample_scale 40 --i_print 5000 --i_img 5000 --i_weights 5000 --i_testset 5000 --i_video 5000'
    os.system(command)
