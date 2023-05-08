awk '{print $2,$1}' data/restauranttest.bio > "./data/test.txt"
awk '{print $2,$1}' data/restauranttrain.bio > "./data/train.txt"
sed -i 's/\t/ /g' './data/test.txt' 
sed -i 's/^ $/\n/g' './data/test.txt'
sed -i 's/\t/ /g' './data/train.txt' 
sed -i 's/^ $/\n/g' './data/train.txt'
python preprocess.py