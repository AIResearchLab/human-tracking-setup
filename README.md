# human-tracking-setup

A human tracking sensor setup for Social Aware Navigation.

To use GPU with docker while on AMD64 systems, install nvidia-container-toolkit with given instructions.

## Installation

```sh
git clone https://github.com/AIResearchLab/human-tracking-setup.git
```

## Startup

```sh
docker compose pull
docker compose up
```

## Stopping

```sh
docker compose down
```

## Remove docker volumes for resetting

```sh
docker compose rm human-tracking-setup_boxmot
```
