{ pkgs ? import <nixpkgs> { } }:
with pkgs;
mkShell {
  name = "slack-weather-bot";
  buildInputs = [
    ngrok
    python38
    python38Packages.poetry
  ];
}
