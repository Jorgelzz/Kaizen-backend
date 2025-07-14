module.exports = {
  apps: [
    {
      name: "kaizen-backend",
      script: "pythonw",
      args: "manage.py runserver 0.0.0.0:8000",
    },
  ],
};
