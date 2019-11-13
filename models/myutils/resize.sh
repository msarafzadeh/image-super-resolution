ls res300 | xargs -I {} convert res300/{} -gravity center -resize 150x150   res150/{}
