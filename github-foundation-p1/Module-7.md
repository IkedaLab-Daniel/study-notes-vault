# Module 7: Manage your work with GitHub Projects

## Unit 1: Introduction
We know your work is dynamic. Priorities can change quickly and needing to stay current and aware of everything is how you and your team can be successful.

Luckily, GitHub Projects can help you stay organized, connected, and up-to-date in order to keep your team on track.

Projects connect your planning directly to the work your team is doing and flexibly adapts to whatever your team needs at any point. Project tables are built like a spreadsheet and give you a live canvas to filter, sort, and group issues and pull requests. You can use Project tables, Project boards, and custom fields to track a sprint, plan a feature, or manage a large-scale release.

Learning objectives:
- Discern the differences between Projects and Projects (Classic)
- Learn how to build an organization level Project
- Understand how to organize your Project
- Gain insight on how to edit the visibility, access, and management of your Project
- Know how to develop automation and insights from your Project

## Unit 2: Projects versus Projects Classic
Let's first go over some of the enhancements in a side-by-side glance and then dive deeper into each section of updates.

The new GitHub Projects provides a richer experience that enables you to keep track of your work, where you work. Let's dive a bit deeper into the changes that have been made.

### Comprehensive lists of Project enhancements

#### Tables and boards
- Plan and track work in a table or board view
- Rank, sort, and group within a table by any custom field
- Create draft issues with detailed descriptions and metadata
- Materialize any perspective with tokenized filtering and saved views
- Customize cards and group-by in Project boards
- Real-time Project updates and user presence indicators

#### Data
- Define custom fields of type: text, number, date, iteration, and single select
- Configure iterations with flexible date ranges and breaks to represent your sprints, cycles, or quarterly roadmap
- View linked pull requests and reviewers in both table and board views

#### Insight
- Create and configure custom bar, column, line, and stacked area charts
- Use aggregation functions like sum, count, average, min, and max to get the proper insight
- Persist charts and share them with a URL to keep everyone in the know

#### Automation
- GraphQL ProjectsV2 API
- GitHub app Project scopes
- Webhooks events for Project item metadata updates
- GitHub Action to automate adding issues to Projects

## Unit 3: How to create a project
Imagine you want to organize your team's feature backlog. Projects, GitHub's built-in program-management tool, is a perfect way to organize and prioritize your team's work in a single space.

### Creating an organization-level Project
First, you want to lay the foundation by creating a new Project. Creating is relatively quick and simple.

1. In the top right corner of GitHub.com, select your profile photo, then select Your organizations.
2. Scroll down to select the organization for your new Project.
3. Navigate from the Overview tab to the Projects tab.
4. Select the green button labeled New Project.
5. A pop-up prompts you to select either a template or start from scratch. Let's choose the Start from scratch option and select Table.
6. Select the green Create project button.

You just created a Project!

You can also create a personal Project by selecting your profile photo and navigating to Your projects. Once you're on your Projects page, select the green button titled New project.

### Set your Project's name, description, and README
Let's define your Project in a couple of different ways so that your team can easily understand what you're tracking.

1. Navigate to your newly created Project to edit your Project's name, description, and README.
2. At the top right of the page, select the three dots to open the menu and select Settings.
3. Project Name is where you edit the name of the Project.
4. Short description allows you to add a few words about the Project.
5. README lets you add information for your team to understand why you created this Project and what you hope to accomplish with it. Once finished, select Save changes.

### Add issues and pull requests to your Project
Adding issues and pull requests to your Project is what makes the tool so powerful. Projects enable you to know the status of tasks your team is working on to coordinate and complete your goals.

#### Add an existing issue and pull request
1. Copy the url of an existing issue or pull request.
2. Place your cursor in the bottom row of the Project next to the + and paste the URL of your issue or pull request.
3. Press Enter and your issue or pull request appears as a task in your Project.

#### Search for an existing issue and pull request
You can search for existing issues or pull requests by adding a new item.

1. Enter # to search repositories. You can type part of the repository name to narrow down your options.
2. Select the repository where the pull request or issue is located, which prompts to search issues and pull requests.
3. Start typing the title of the issue or pull request to find the one you want.
4. Select the issue or pull request.

#### Bulk add issues and pull requests
You can bulk add issues and pull requests to an existing repository to save time. It allows you to start organizing your team faster.
1. Select + in the bottom row of the Project.
2. Select Add item from repository.
3. To change the repository, select the dropdown and choose a repository. The issues and pull requests then populate.
4. You can either select all or select those issues or pull requests you want to include.
5. Once you're ready to add the issues and pull requests to your Project, select the green button titled Add selected items in the bottom right corner.

## Unit 4: How to organize your project

### Create a field to track and group by priority
To group a set of issues and pull requests by priority, you need to first create a new field.

1. In the table view, in the rightmost field header, select +.
2. Select New field.
3. Type the name of your field. In this case, it's Priority.
4. Select the Field Type drop-down.
5. To create your own classification for your new field, select the Single select option.
6. In the Options text box, start to add your different priority levels. You can label them as Urgent, High, Medium, and Low.
7. Select Save.

Now that you have your priority classification set up, you need to classify your issues and pull requests based on priority. To make a classification, select the issue or pull request you want to classify in the field row titled Priority. Now, in the drop-down field, select the priority you want to choose for this particular issue or pull request.

Repeat for your remaining pull requests and issues.

Now, let's group your issues and pull requests by priority to make it easier to focus on urgent and high priority items.

1. Select the down arrow next to the name of your currently opened view.
2. Select the Group by option.
3. Select Priority.

Now you should be able to view issues and pull requests based on the priority you assigned them. One of the great features of this particular view is you can now drag and drop issues into new priority fields easily.

### Add an iteration field
Adding an iteration field to your Project can help you and your team visualize the balance of upcoming work in order to help everyone stay on track. An iteration field enables you to set up phases for your tasks in a tangible timeframe to keep you and your team organized.

1. To add an iteration field, go to your Project's table view.
2. In the rightmost field header, select +.
3. Select New field.
4. Add a Field name, such as Project Phase or Sprint.
5. Under Field Type, select Iteration.
6. Choose a Starts On date.
7. Change the Duration of each iteration by typing a new number, and select the drop-down for either days or weeks as follows.
8. Select Save and create.

Once you have your iteration field set up, you can now assign what iteration phase you want each of your issues and pull requests to fall under.

### Create a board view
A board view of your Project enables you to view upcoming tasks in a more visual way.

Let's walk through how to get your board view up and running.
1. On the currently open view, select the down arrow.
2. Under Layout, select Board. When you change the layout, your Project displays an indicator to show the view was modified.
3. Select the Save button at the top-right of the board.
4. You can rename the view by double-clicking the view's tab, and selecting out of the tab to automatically save.
5. Note these steps can also be accomplished by selecting New View to the right of your existing views.

Now, you can drag and drop issues and pull requests to the various columns.