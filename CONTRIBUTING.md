# Contribution guidelines
- [Open issues](#open-issues)
- [Add a developer](#add-a-developer)
  - [Developer template](#developer-template)
  - [Pull request](#pull-request)
- [Open issues](#open-issues)

Only add developers that are **awesome**! *"After all, it's a curation, not a collection"*. [What is awesome?](https://github.com/sindresorhus/awesome/blob/main/awesome.md#only-awesome-is-awesome)
It doesn't matter if the developer isn't active anymore; if the developer has a profile but no new projects, it still counts.

## Add a developer
To add a developer, you will need to create a pull request from a forked repository. 

- On the upper right, click on the fork button 
- In the fork you've created, create a new branch (if you're using command line, do: `git checkout -b NAME_OF_BRANCH`)
- Edit the `developers.json` file in the branch you've just created. 
- Using the developer template down below, add the developer(s) to the appropriate section **at the bottom of the section**  or create another section if you need to (a section holds several developers, please use discretion). 

*Jump to the [Pull request template](#pull-request-template) to know how to open a pull request*.

How to use the developer template: 
- Do not use link shorteners
- Do not change any layout or attributes in the template
- Fill out the template with developer information replacing items in ALL_CAPS and the featured projects and languages sections
- The link to the profile must redirect only to the developers main profile (it **shouldn't** redirect to one of their projects) (eg. https://github.com/roaldnefs or https://gitlab.com/roaldnefs). 
- To get the avatar of the profile, go to the main profile's page, right-click the avatar and select "copy image adress". Paste the image address to replace the LINK_TO_THE_AVATAR_OF_THE_PROFILE in the template.
- If the profile meets any badge requirements, add accordingly (refer to [BADGES.md](https://github.com/roaldnefs/awesome-developers/blob/main/BADGES.md)). If the develop doesn't meet badge(s) requirements, delete that badge option. Developers do not need to meet any badge requirement.
- The "languages" section **should not** be more than **1** line.
- The "featured" section **should not** be more than **2** lines. 
  - If the developer doesn't have any of it's own projects, you can consider a series of projects the developer contributed to as a featured project or type "`None`".

### Developer template
```json
{
    "name": "NAME_OF_THE_DEVELOPER",
    "avatar": "LINK_TO_THE_AVATAR_OF_THE_DEVELOPER",
    "profile": "LINK_TO_THE_PROFILE_OF_THE_DEVELOPER",
    "ghstar": "OPTIONAL_LINK_TO_GITHUB_STARS_PROFILE",
    "languages": ["LANGUAGE", "LANGUAGE"],
    "featured": [
        {
            "name": "NAME_OF_THE_PROJECT",
            "link": "LINK_TO_THE_PROJECT"
        }
    ]
}
```

### Pull request
When you finished adding the developer profile(s) on the forked repository, open a pull request. 

To open a pull request:
- Go to the [Pull request section in this repository](https://github.com/roaldnefs/awesome-developers/pulls)
- Click on "New pull request" 
- Click on "compare across forks". 
- Change the two options on the right-hand side of the arrow "<-" icon to be the fork you've created (it should be `your_github_username/awesome-developers`) and the branch you've created in your fork. **Don't change the two options on the left (whose should be "base repository: roaldnefs/awesome-developers" and "base: main".)** 
- Fill it with the proper information.
- Click on "Create pull request"

You can add any number of developers at a time in just one pull request.

## Open issues
If you find a layout issue, a typo or an outdated information about a developer, please open an issue explaining what it is about.
If you have an idea of a possible feature, please also open an issue explaining your idea.
The issue labels are assigned accordingly to every issue - follow them to know more about the issue