#Task Management Web App

Build the images and spin up the containers:

```sh
$ docker-compose up -d --build
```

Apply the migrations:

```sh
$ docker-compose exec backend aerich upgrade
```

Ensure [http://localhost:8000](http://localhost:8000), [http://localhost:8000/docs](http://localhost:8000/docs), and [http://localhost:3000](http://localhost:3000) work as expected.
