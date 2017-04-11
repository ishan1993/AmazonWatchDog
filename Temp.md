User - "add_product <URL> <price> <tag>"
add_product will add URL to json

#deamon
2 hours freq
script reads and parses json
3-D list 
[[URL,price,tag1],[URL2,price2,tag2]]
list iterate 
TCP socket -> req amazon server
HTML parse -> get price
compare vs user_threshold
if (low) -> notification with tag and URL
