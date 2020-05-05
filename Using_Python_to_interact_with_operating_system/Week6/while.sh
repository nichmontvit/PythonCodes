n = 1
# using $1 is the same as doing sys.argv[1]
command = $1
while ! $command && [ $n -le 5 ]; do
    sleep $n
    echo "Iteration number $n"
    ((n+=1))
    echo "Retry #$n"
done;