# find . -name '*' -exec identify -format '%w %h\n' '{}' \; 
#find . -name '*' -exec identify -format '%w %h\n' '{}' \; | awk -F' ' '$1 > 500 && $2 > 500' 
find image-super-resolution/data/imagenet/orig/ -name '*' -exec identify -format '%i %w %h\n' '{}' \; | awk -F' ' '$2 > 300 && $3 > 300 {print;}'
#find . -name '*' -exec identify -format '%i %wx%h\n' '{}' \;
