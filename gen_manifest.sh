#!/usr/bin/env bash

jq ".features.slash_commands[0].url = \"${1}/slack/events\"" manifest.json
