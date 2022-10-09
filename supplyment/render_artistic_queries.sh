#!/bin/bash

datasets=( lego )
queries=( "Concept art %s; trending on artstation; Unreal Engine" "Pencil sketch %s; Art on Instagram" "Neolithic cave painting %s" "Red %s" )

for dataset in "${datasets[@]}"
do
  for i in "${!queries[@]}"
  do
    printf -v formatted_query "${queries[$i]}" "${dataset}"
    printf -v expname "%s-%d" "${dataset}" ${i}
    python run_nerf_clip.py --expname ${expname} --config configs/${dataset}.txt --use_clip --w_clip 1.0 --description \"\'${formatted_query}\'\" --ft_path checkpoints/${dataset}.tar --sample_scale 40 --i_print 5000 --i_img 5000 --i_weights 5000 --i_testset 5000 --i_video 5000
  done
done
