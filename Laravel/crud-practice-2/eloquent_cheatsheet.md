# Laravel Eloquent Cheatsheet

A quick reference for the most common Eloquent model methods used in controllers for CRUD (Create, Read, Update, Delete) operations.

## Retrieving Multiple Records

*   `Model::all()`
    *   **What it does:** Gets every single record from the model's table.
    *   **When to use:** Good for small tables, but be careful with large amounts of data.

*   `Model::where('column', 'value')->get()`
    *   **What it does:** Filters records based on a condition. The `get()` method executes the query and returns a collection of results. You can chain multiple `where()` calls.
    *   **Example:** `Note::where('status', 'published')->get()`

*   `Model::latest()->get()`
    *   **What it does:** A shortcut for ordering records by the `created_at` column in descending order (newest first).

## Retrieving a Single Record

*   `Model::find($id)`
    *   **What it does:** Finds one record by its primary key (the `id`). Returns `null` if nothing is found.

*   `Model::findOrFail($id)`
    *   **What it does:** Same as `find`, but if no record is found, it automatically throws a "404 Not Found" error. This is a best practice for controllers.

*   `Model::where('column', 'value')->first()`
    *   **What it does:** Executes a query and gets only the very first result that matches.

## Creating and Updating Records

### Creating

*   `Model::create($attributes)`
    *   **What it does:** Creates and saves a new record in a single line.
    *   **Security Note:** This requires you to define which fields are "fillable" in your model file for security (mass-assignment protection).
    *   **Example in `Note.php`:** `protected $fillable = ['title', 'message', 'user_id'];`

### Updating

*   `$model = Model::find($id);`
    `$model->property = 'New Value';`
    `$model->save();`
    *   **What it does:** A two-step process. You retrieve a model, change its properties, and then `save()` the changes back to the database.

## Deleting Records

*   `$model = Model::find($id);`
    `$model->delete();`
    *   **What it does:** Finds a record and then deletes it.

*   `Model::destroy($id)`
    *   **What it does:** Deletes a record by its primary key without needing to retrieve it first. Can also accept an array of IDs to delete multiple records.
