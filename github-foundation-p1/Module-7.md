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

## Unit 5: How to organize and automate your project

### Control visibility to your Project
You have the ability to control whether your Project is public or private. When your Project is public, everyone on the internet can view it. When your Project is private, only users granted at least read access can see your Project.

To change your Project's visibility:
1. Navigate to your Project.
2. In the top-right, select the three dots at the top menu and choose Settings.
3. Scroll down to Danger zone, and under Visibility select Private or Public from the drop-down.

### Manage access to your Project
Access to your Project depends on if your Project is an organization-level Project or a personal/user-level Project. Managing access is similar between the two levels.

Admins of organization-level Projects can manage access for the entire organization, for teams, for individual organization members, and for outside collaborators. Admins of user-level Projects can invite individual collaborators and manage their access.

#### Organization-level Project
- No access: Only organization owners and users granted individual access can see the Project. Organization owners are also admins for the Project.
- Read: Everyone in the organization can see the Project. Organization owners are also admins for the Project.
- Write: Everyone in the organization can see and edit the Project. Organization owners are also admins for the Project.
- Admin: Everyone in the organization is an admin for the Project.

#### Personal/User-level Project
- Read: The individual can view the Project.
- Write: The individual can view and edit the Project.
- Admin: The individual can view, edit, and add new collaborators to the Project.

### Invite collaborators and change roles
1. Navigate to your Project.
2. In the top right, select the three dots to open the menu and choose Settings.
3. In the left-hand navigation bar, select Manage access.
4. Once on the page you can either:
- Invite individuals and teams by searching in the Invite collaborators search bar.
- Change their role or remove them under Manage access.

### Add a Project to a team
You can add Projects to your team to give them collaborator access to their Projects. Adding lists them on the team's Projects page, which makes it easier for members to identify which Project a particular team uses. Teams are granted read permissions on any Project they get added to.

### Add a Project to a repository
You can list relevant Projects in a repository so your team can access information they need to stay up to date. However, you can only list Projects if the same user or organization owns both the Projects and the repository. In order for repository members to see a Project listed in a repository, they must have visibility to the Project.

### Close and delete Projects
Once you complete a Project or you no longer need to use it, you can either close or delete it.

Closing a Project enables you to remove it from the list of Projects but retain the content and ability to reopen the Project later. We recommend this option to preserve your data.

However, deleting a Project permanently removes it from the platform along with any saved views, custom fields and associated values, insights data, and drafted issues.

Regardless of which option you choose, both closing and deleting Project settings are in the same location.

## Unit 6: Insight and automation with projects

### Insights and how they can be useful
Insights with Projects enables you to view, create, and customize charts that use items added to your Project as source data. When you create a chart, you set the filters, chart type, and information displayed. The chart is available to anyone who can view the Project. You can generate two types of charts: current charts and historical charts. Let's dive into the differences between the two.

### Current charts
You can create current charts to visualize your Project items. For example, you can create charts to show the number of items assigned to each individual, or the number of issues assigned to each upcoming iteration.

You can use filters to manipulate the data used to build your chart. For example, you can create a chart showing how much upcoming work you have, but limit those results to particular labels or assignees.

### Historical charts
Historical charts are available with GitHub Team and GitHub Enterprise Cloud for organizations. Historical charts are time-based charts that allow you to view your Project's trends and progress. You can view the number of items over time grouped by status and other fields. The default Burn up chart shows item status over time, allowing you to visualize progress and spot patterns.

### Create and customize charts
Follow these steps to create a new chart:
1. Navigate to your Project.
2. In the top-right, select the line graph button. When you hover over the button, the Insights label appears.
3. In the menu on the left, select New chart.
4. Filter by keyword or field to change the data used to build the chart.
5. To the right of the filter text box, select Save.

Now that you created a new chart, let's customize your new chart to fit your needs.
1. In the menu on the left, select the chart you'd like to configure.
2. On the right side of the page, select Configure, and a panel opens.
3. Select the Layout dropdown to change the type of chart you want to use.
4. Select the X-axis dropdown and choose the field you want to use.
5. Optionally, select Group by to group items on your X-axis. Choose the field you want to use or None to disable grouping.

### Automation with Projects
There are three different ways you can do so:
1. Built-in automated workflows
2. GraphQL API
3. GitHub Actions with workflows
The easiest way to automate your Project is built-in workflows. GraphQL and Actions give more control over customizing automation.

### Configure built-in workflows
Built-in workflows help you stay aware of all your work. Your Project takes newly created issues or pull requests and automatically puts them into your Project with a Todo status. Here's how to enable:

1. In the top-right corner of your Project, select the three dots menu and choose Workflows.
2. In the left column, under Default workflows, select Item added to project.
3. Select the Edit button to make changes to the workflow.
4. In the When an item is added to the project section, ensure that both issues and pull requests are selected.
5. In the Set Value section, select Status:Todo.
6. Select Save and turn on workflow.

### GitHub Actions with workflows
GitHub Actions enables the most customization for your Project's automation. You can use GitHub Actions to automate your project management tasks by creating workflows. Each workflow contains a series of tasks that are performed automatically every time the workflow runs. An example workflow triggers upon issue creation that adds a label, leaves a comment, and moves the issue to a project board.

An issue creation triggers a workflow that adds a label, leaves a comment, and moves the issue to a project board.

GraphQL API
If you're using GraphQL in GitHub, you can utilize an API to help automate your Project

