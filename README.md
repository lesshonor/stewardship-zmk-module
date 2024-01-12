## Instructions

Add this repository to your existing `config/west.yml` as shown below. (No idea what that means? [Make a new repo from this template first](https://github.com/zmkfirmware/unified-zmk-config-template), and [go read the docs](https://zmk.dev/docs/customization#building-additional-keyboards)!)

```yaml
manifest:
  remotes:
    - name: zmkfirmware
      url-base: https://github.com/zmkfirmware
    # Add the base GitHub URL as a remote.
    - name: lesshonor # You can name this whatever you like; just make sure the "remote" below matches.
      url-base: https://github.com/lesshonor
  projects:
    - name: zmk
      remote: zmkfirmware
      revision: main
      import: app/west.yml
    # Add the name of the repository as a project.
    - name: stewardship-zmk-module
      remote: lesshonor
      revision: main # This is the name of the branch you want to use.
  self:
    path: config
```

After making this change, copy any keymaps you may need out of the appropriate board and/or shield folders and paste them into your `config` folder for later modification. Don't forget to [edit your `build.yaml` to include them](https://zmk.dev/docs/customization#building-additional-keyboards), too.

## Explainer

|                           | Knowledge of ZMK | Desire to maintain keyboard firmware |
|---------------------------|------------------|--------------------------------------|
| ZMK maintainers           | :100:            | :x:                                  |
| Keyboard creators/vendors | :question:       | :question:                           |
| Owner of keyboard         | :question:       | :100:                                |

In a perfect world, *someone* would have a :100: in both of those columns; a high level of ZMK expertise, and a strong desire to ensure a keyboard's firmware remains usable.

...A lot of people live in a world where:
- The creator[^1] cut-pasted together code that *just barely* compiled through a verbose haze of deprecation warnings
- The ZMK maintainers have since moved the codebase to an entirely different version of Zephyr
- The vendor[^1] never had any idea how the firmware worked from jump

[^1]: In this scenario, it is entirely possible for the creator and vendor to be the same individual.</sup>

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
- Ask the ZMK experts in [ZMK's Discord](https://zmk.dev/community/discord/invite)
