"use server";

import { AsyncDatabase } from "promised-sqlite3";

export default async function postNote (formData) {
    console.log("PostNote called", formData)

    const from = formData.get("from_user");
    const to = formData.get("to_user")
    const note = formData.get("note")

    if (!from || !to || !note) {
        throw new Error("wtf i need payload")
    }

    
}