# Dynamatic in vscode

## Configure GDB for Dynamatic

We can only debug one Dynamatic pass at a time. We need specific extensions for running debugger, namely, the official `C/C++` and `C/C++ Extension Pack` extensions from Microsoft.

Goto the `.vscode` directory, and create a `launch.json` file.

```json
{
  "version": "0.2.0",
  "configurations": [
      {
          "name": "Debug Pass",
          "type": "cppdbg",
          "request": "launch",
          "program": "${workspaceFolder}/bin/dynamatic-opt", // Path to the binary
          "args": [
              "${workspaceFolder}/integration-test/fir/out/comp/handshake_export.mlir",
              "--handshake-set-buffering-properties=version=fpga20",
              "--handshake-place-buffers=algorithm=fpga20 frequencies=${workspaceFolder}/integration-test/fir/out/comp/frequencies.csv timing-models=${workspaceFolder}/data/components.json target-period=6.0 timeout=300 dump-logs"
              ],
          "stopAtEntry": false,
          "cwd": "${workspaceFolder}", // Set working directory
          "environment": [],
          "externalConsole": false,
          "MIMode": "gdb",
          "miDebuggerPath": "/usr/bin/gdb", // Path to gdb
          "setupCommands": [
              {
                  "description": "Enable pretty-printing for gdb",
                  "text": "-enable-pretty-printing",
                  "ignoreFailures": true
              }
          ],
          "preLaunchTask": "",
          "postDebugTask": "",
          "logging": {
              "moduleLoad": false,
              "programOutput": true,
              "engineLogging": false,
              "trace": false
          }
      }
  ]
}
```

After saving this, we can launch debugger by `Ctrl-Shift-D`.
