import os

scenes = {
  "chair": {
    "dataset": "chair",
    "article": "a",
    "name": "chair",
    "source_prompt": "A green chair"
  },
  "hotdog": {
    "dataset": "mic",
    "article": "a",
    "name": "microphone",
    "source_prompt": "A silver microphone"
  },
  "lego": {
    "dataset": "lego",
    "article": "a",
    "name": "excavator",
    "source_prompt": "A yellow lego excavator"
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
    command = f'python run_nerf_clip.py --expname {scene["dataset"]}_{query["name"]}_comparison --config configs/{scene["dataset"]}.txt --description "{current_query}" --source_prompt "{scene["source_prompt"]}" --sample_scale 40 --render_only --render_test'
    print(f'[RUNNING] {command}')
    os.system(command)
