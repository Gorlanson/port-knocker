cat input.txt | while read line
do
        echo $line | sed -e 's|^[^/]*//||' -e 's|/.*$||' >> list.txt
done
