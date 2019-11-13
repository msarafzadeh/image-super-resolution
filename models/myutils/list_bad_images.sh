find image-super-resolution/data/imagenet/orig/ | while read FILE; do
    if ! identify "$FILE" &> /dev/null; then
        echo "$FILE"
    fi  
done
