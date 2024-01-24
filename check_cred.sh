cont=1

for arg in "$@"; do
    echo "Testing argument $cont"
    exist=$(grep -ri --exclude-dir=".git" --exclude-dir="__pycache__" --exclude-dir="venv" "$arg" .)
    if [ -n "$exist" ]; then
        echo $exist
        echo "Unsafe package password found"
        exit 1
    else
        cont=$((cont + 1))
    fi
done

echo "No credentials found 🎉"

exit 0