#!/bin/sh

environment='test'
maven="mvn -P$environment"

source='' #eventuale path aggiuntivo per arrivare al source del progetto
install="$maven install -Dmaven.test.skip"

declare -a report=("Build digest" "------------")

function build {
        project=$1
        cd "$project$source"
        branch=$(git rev-parse --abbrev-ref HEAD)
        revision=$(git rev-parse --short HEAD)
        when=$(git show -s --format=%ci $revision)
		s="$count. building $1 [$branch] [$revision] [$when] ..."
        echo $s; report+=("$s")
        $install; cd ../..
        ((++count))
}

count=1
echo 'Begin building'

build 'project1_directory'
build 'project2_directory'
build 'project3_directory'

echo 'End building'
echo
for line in "${report[@]}"; do echo $line; done