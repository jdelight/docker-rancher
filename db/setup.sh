#!/usr/bin/env bash

createuser -U postgres --createdb --createrole dbuser;
createdb -U dbuser films;
