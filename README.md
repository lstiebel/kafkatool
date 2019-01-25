# Command line tool to manage Kafka topics, consumer groups and their offsets

## Usage

```
usage: kafkatool.py [-h] [-b HOST] [-o BROKER_VERSION] [-s SSL_ENABLED]
                    {consume_topic,desc_topic,print_consumer_groups,print_consumer_lag,print_offsets,print_topics,reset_offsets,create_topic,delete_topic}
                    ...

CLI tool for Kafka.

positional arguments:
  {consume_topic,desc_topic,print_consumer_groups,print_consumer_lag,print_offsets,print_topics,reset_offsets,create_topic,delete_topic}
                        Commands
    consume_topic       Dump messages for a topic to a file or stdout.
    desc_topic          Print detailed info for a topic.
    print_consumer_groups
                        Get consumer groups for a topic
    print_consumer_lag  Get consumer lag for a topic.
    print_offsets       Fetch broker offsets for a topic
    print_topics        Print information about all topics in the cluster.
    reset_offsets       Reset offsets for a topic/consumer group
    create_topic        Create a topic
    delete_topic        Delete a topic

optional arguments:
  -h, --help            show this help message and exit
  -b HOST, --broker HOST
                        host:port of any Kafka broker. [default:
                        localhost:9092]
  -o BROKER_VERSION, --broker_version BROKER_VERSION
                        The version string of the broker with which to
                        communicate. [default: 2.1]
  -s SSL_ENABLED, --ssl-auth SSL_ENABLED
                        Use SSL authentication. Set to true or false. Provide
                        CA, client cert and key file via environment
                        variables. [default: false]
```

## Installation

Run `sudo python3 setup.py install` (in the `kafkatool` subdirectory). This installs all dependencies and places kafkatool into your `$PATH` and allows you to run `kafkatool.py --help` without prefixing the location of the script.

Alternatively, you can also use the docker image `capturemedia/kafkatool` via:

```
docker run --rm -it -v /dir/with/ssl/certs:/ssl -e KAFKA_SSL_CA_FILE=/ssl/ca.crt -e KAFKA_SSL_CLIENT_CERT=/ssl/client.crt -e KAFKA_SSL_CLIENT_KEY=/ssl/client.key capturemedia/kafkatool:latest --ssl-auth true ...
```

## SSL client authentication

To enable SSL client authentication via certificate and key use the argument `-s true` or `--ssl-enabled true`.

Specify the locations of the CA certificate (`KAFKA_SSL_CA_CERT`), client certificate (`KAFKA_SSL_CLIENT_CERT`) and key (`KAFKA_SSL_CLIENT_KEY`) files as environment variables.

## Arguments

### `consume_topic`
Parameters:
```
topic
```
### `desc_topic`
Parameters:
```
topic
```
### `print_consumer_groups`
Parameters:
```
topic
```
### `print_consumer_lag`
Parameters:
```
topic
consumergroup
```
### `print_offsets`
Parameters:
```
topic
```
### `print_topics`
Parameters:
```
None
```
### `reset_offsets`
Parameters:
```
topic
consumergroup
```
### `create_topic`
Parameters:
```
topic
num_partitions
replication_factor
```
### `delete_topic`
Parameters:
```
topic
```