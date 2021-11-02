{ pkgs ? import <nixpkgs> { } }:
with pkgs;
mkShell {
  name = "slack-weather-bot";
  buildInputs = [
    python38
    python38Packages.poetry
  ];
}
