### A basic Gnome Builder "hello world" using Gnome 47 runtime

I created this project with the following steps:

1. Launch Gnome Builder 42.0 on Linux Mint 21.3 Cinnamon.
2. Select "Start New Project".
3. Select language: "Python"
4. Select a template: "GTK Application"
5. Create the project
6. Edit the manifest, changing "runtime-version" from "master" to "47".
7. Building (Ctrl-F5) and running the application (Ctrl-F7) works just fine, we see a window with "Hello World"

### Problem: Create the flatpak in the terminal

When we compile in Gnome Builder with Ctrl-F7, the information pane displays the following:

```
flatpak build --env=TERM=xterm-256color --env=V=0 --env=CCACHE_DIR=/home/jr/.cache/gnome-builder/flatpak-builder/ccache --env=FLATPAK_CONFIG_DIR=/home/jr/.local/share/gnome-builder/flatpak/etc --env=PATH=/app/bin:/usr/bin --env=G_MESSAGES_DEBUG= --env=XDG_RUNTIME_DIR=/run/user/1000 --build-dir=/home/jr/.cache/gnome-builder/projects/gnome_47_test/builds/org.bswa.Gnome47Test.json-flatpak-org.gnome.Platform-47-x86_64-master --share=network --nofilesystem=host --filesystem=/home/jr/.cache/gnome-builder --filesystem=/home/jr/Code/gnome_47_test --filesystem=/home/jr/.cache/gnome-builder/projects/gnome_47_test/builds/org.bswa.Gnome47Test.json-flatpak-org.gnome.Platform-47-x86_64-master --env=NOCONFIGURE=1 /home/jr/.cache/gnome-builder/projects/gnome_47_test/flatpak/staging/x86_64-master ninja
ninja: no work to do.
```

I'd like to do the same thing in the terminal. Based on the flatpak docs, I'm using the following command:

`$ flatpak-builder --force-clean --user --repo=repo builddir org.bswa.Gnome47Test.json`

Having upgraded `flatpak-builder` to version `1.4.4` I get the following error:

```
Running appstreamcli compose
Only accepting components: org.bswa.Gnome47Test, org.bswa.Gnome47Test.desktop
Processing directory: /home/jr/Code/gnome_47_test/.flatpak-builder/rofiles/rofiles-CMwPv0/files
Composing metadata...
Run failed, some data was ignored.
Errors were raised during this compose run:
org.bswa.Gnome47Test.desktop
  E: metainfo-no-summary
Refer to the generated issue report data for details on the individual problems.
Error: ERROR: appstreamcli compose failed: Child process exited with code 1
```
