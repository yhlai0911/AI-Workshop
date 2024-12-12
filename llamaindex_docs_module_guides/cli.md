# CLI#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/50_llamactl/

# CLI#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/50_llamactl/#cli)

llamactl is a command line interface that ships with Llama Deploy and has the main goal to easily interact with a
running [API Server](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/20_core_components/#api-server).

```
llamactl
```

# llamactl#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/50_llamactl/#llamactl)

Usage:

```
llamactl [OPTIONS] COMMAND [ARGS]...
```

```
llamactl [OPTIONS] COMMAND [ARGS]...
```

Options:

```
--version            Show the version and exit.
  -s, --server TEXT    Apiserver URL
  -k, --insecure       Disable SSL certificate verification
  -t, --timeout FLOAT  Timeout on apiserver HTTP requests
  --help               Show this message and exit.
```

```
--version            Show the version and exit.
  -s, --server TEXT    Apiserver URL
  -k, --insecure       Disable SSL certificate verification
  -t, --timeout FLOAT  Timeout on apiserver HTTP requests
  --help               Show this message and exit.
```

## llamactl deploy#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/50_llamactl/#llamactl-deploy)

Usage:

```
llamactl deploy [OPTIONS] DEPLOYMENT_CONFIG_FILE
```

```
llamactl deploy [OPTIONS] DEPLOYMENT_CONFIG_FILE
```

Options:

```
--help  Show this message and exit.
```

```
--help  Show this message and exit.
```

## llamactl run#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/50_llamactl/#llamactl-run)

Usage:

```
llamactl run [OPTIONS]
```

```
llamactl run [OPTIONS]
```

Options:

```
-d, --deployment TEXT     Deployment name  [required]
  -a, --arg <TEXT TEXT>...  'key value' argument to pass to the task, e.g. '-a
                            age 30'
  -s, --service TEXT        Service name
  -i, --session-id TEXT     Session ID
  --help                    Show this message and exit.
```

```
-d, --deployment TEXT     Deployment name  [required]
  -a, --arg <TEXT TEXT>...  'key value' argument to pass to the task, e.g. '-a
                            age 30'
  -s, --service TEXT        Service name
  -i, --session-id TEXT     Session ID
  --help                    Show this message and exit.
```

## llamactl sessions#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/50_llamactl/#llamactl-sessions)

Usage:

```
llamactl sessions [OPTIONS] COMMAND [ARGS]...
```

```
llamactl sessions [OPTIONS] COMMAND [ARGS]...
```

Options:

```
--help  Show this message and exit.
```

```
--help  Show this message and exit.
```

### llamactl sessions create#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/50_llamactl/#llamactl-sessions-create)

Usage:

```
llamactl sessions create [OPTIONS]
```

```
llamactl sessions create [OPTIONS]
```

Options:

```
-d, --deployment TEXT  Deployment name  [required]
  --help                 Show this message and exit.
```

```
-d, --deployment TEXT  Deployment name  [required]
  --help                 Show this message and exit.
```

## llamactl status#

[#](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/50_llamactl/#llamactl-status)

Usage:

```
llamactl status [OPTIONS]
```

```
llamactl status [OPTIONS]
```

Options:

```
--help  Show this message and exit.
```

```
--help  Show this message and exit.
```

