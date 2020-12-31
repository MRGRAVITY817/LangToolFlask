docker run \
  -v $(pwd)/app:/app \
  --name grammar-ai \
  -p 5000:5000 \
  -it --rm mrgravity817/grammar
