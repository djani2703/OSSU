marco () {
    echo $(pwd) > /tmp/marco_tmp_path
}

polo () {
    cd "$(cat /tmp/marco_tmp_path)"
}