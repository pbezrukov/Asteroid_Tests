# Asteroid_Tests


## **Setup**
```
git clone https://github.com/pbezrukov/Asteroid_Tests.git
cd path/to/Asteroid_Tests
docker build -t asteroid .
```

## **Run tests**

```docker run -p 5000:5000 -it -v $(pwd)/results:/results asteroid```

***
## **Look of report**

Open browser and go to url ```localhost:5000```
