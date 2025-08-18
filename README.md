## Instructions

Add this repository to your existing `config/west.yml` as shown below[^1]. (No idea what that means? [Make a new repo from this template first](https://github.com/zmkfirmware/unified-zmk-config-template)!)

[^1]: Your `zmk`/`zmkfirmware` repository may look a bit different. You may have other projects in your [west manifest](https://docs.zephyrproject.org/latest/develop/west/manifest.html#manifest-files). That's fine; leave those alone.

```yaml
  projects:
    - name: zmk
      remote: zmkfirmware
      revision: main
      import: app/west.yml
    ### BEGIN CHANGES ###
    - name: zmk-module-lesshonor
      url: https://github.com/lesshonor/stewardship-zmk-module
      revision: main
    ###  END CHANGES  ###
  self:
    path: config
```

After editing this file, copy any [keymaps](https://github.com/search?q=repo%3Alesshonor%2Fstewardship-zmk-module%20path%3A%2F.%2B%5C.keymap%24%2F&type=code) you need into your repository's `config` folder for later modification. Don't forget to [edit your `build.yaml` to include the keyboards you want to build](https://zmk.dev/docs/customization#building-additional-keyboards), too.

### Common Features

- [Keymap Editor](https://nickcoutsos.github.io/keymap-editor/) layout definitions live under [`assets/json`](assets/json).

### Versioning

This repository tracks ZMK `main`, as the vast majority of changes to ZMK will have no affect on its contents. If desired, `revision` can be pinned to a specific commit hash:

```yaml
    - name: zmk-module-lesshonor
      url: https://github.com/lesshonor/stewardship-zmk-module
      revision: 23faa87 # IYKYK
```

## Background

|                           | Knowledge of ZMK | Desire to maintain keyboard firmware |
|---------------------------|------------------|--------------------------------------|
| ZMK maintainers           | :100:            | :x:                                  |
| Keyboard creators/vendors | :question:       | :question:                           |
| Owner of keyboard         | :question:       | :100:                                |

In a perfect world, *someone* would have a :100: in both of those columns; a high level of ZMK expertise, and a strong desire to ensure a keyboard's firmware remains usable.

...A lot of people live in a world where:
- The creator[^2] cut-pasted together code that *just barely* compiled through a verbose haze of deprecation warnings
- The ZMK maintainers have since moved the codebase to an entirely different version of Zephyr
- The vendor[^2] never had any idea how the firmware worked from jump

[^2]: In this scenario, it is entirly possible for the creator and vendor to be the same individual.

Sometimes these people politely ask me for help. Sometimes "these people" are me. Either way:

|      | Knowledge of ZMK   | Desire to maintain keyboard firmware |
|------|--------------------|--------------------------------------|
| Me   | :white_check_mark: | :white_check_mark:                   |

We're not exactly at :100: here, but better than nothing.

If a keyboard (board or shield) is in this repo, chances are:
- I had to create it, fix it for somebody or help somebody fix it, and I might as well save my work.
- I own it, I intend to continue using it, and I have some concerns about the willingness and/or ability of the creator/vendor to maintain it.

Caveat builder: if I don't own it, I can't test it, and it may be broken in subtle or major ways. I would love to assure you of something more than "hey, it builds!", but that's literally impossible. Sorry.

## Further Troubleshooting Resources

- [ZMK's troubleshooting page](https://zmk.dev/docs/troubleshooting)
- [Zephyr's devicetree troubleshooting page](https://docs.zephyrproject.org/latest/build/dts/troubleshooting.html)
- Ask the ZMK experts in [ZMK's Discord](https://zmk.dev/community/discord/invite)
