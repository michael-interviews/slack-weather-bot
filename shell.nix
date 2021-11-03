{ pkgs ? import <nixpkgs> { } }:
with pkgs;
mkShell {
  name = "slack-weather-bot";
  buildInputs = [
    jq
    ngrok
    python38
    python38Packages.poetry
  ];
}
