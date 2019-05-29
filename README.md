# RequestServer

The server that manages requests from arbitrary apps.

All requests are sent through UDP as short json strings.
All requests look like this:
```
{
	"intent" : <string>,
	"paramaters" : <list of variants>
}
```

The table below details all possible requests with their parameters.

The list of the parameters must be in the order specified below to work.


| Request | Parameters | Description |
|---------|----------  |-------------|
| time    | n/a        | Returns the current time |
