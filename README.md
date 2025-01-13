# Application de détection du cancer du sein à partir de la mammographie.

The model should be put inside the [assets/model](./assets/model/) directory and the mammograms should be put inside the [assets/mammograms](./assets/mammograms/) directory.

Source code is under the [src](./src/) folder

## Model

You can get a picked model from [here](https://github.com/gomu-gomu/ma-dl-projet-1/releases/latest).
get both `X_test.pkl` and `y_test.pkl` and put them inside the [assets/model](./assets/model/) directory.

## Usage

The app can be run via:

```sh
streamlit run src/__main__.py
```

## Docker

This demo comes in with a docker image that can be run with:

```sh
./scripts/run.sh
```