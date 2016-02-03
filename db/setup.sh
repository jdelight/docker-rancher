#!/usr/bin/env bash

createuser -U postgres --createdb --createrole $DB_USER;
createdb -U $DB_USER $DB_NAME;
