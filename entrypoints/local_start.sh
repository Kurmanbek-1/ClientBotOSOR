echo "1. Docker compose up build"
echo "2. Docker compose up"

echo "Checking for shared network..."
if [ -z "$(docker network ls | grep shared_network)" ]; then
    echo "Creating shared_network..."
    docker network create shared_network
else
    echo "shared_network already exists."
fi

read -n1 -p "Pick option? [1,2]: " doit
echo
case $doit in
  1) echo "Running Docker Compose with Build..."
     cd ../ && docker compose -f docker-compose.yml up --build;;

  2) echo "Running Docker Compose without Build..."
     cd ../ && docker compose -f docker-compose.yml up;;
  *) echo "Invalid option selected." ;;
esac
