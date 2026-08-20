# Gen AI 20-Hour Plan — Progress Tracker

A single-file HTML progress tracker for the CampusX "Generative AI using LangChain" playlist. It's a public, read-only progress page for anyone who visits, with a hidden owner login that lets you (and only you) check off videos and log partial progress.

## What it is

The whole app lives in one file, `index.html` — no build step, no server code. It's a static page that talks directly to a [Supabase](https://supabase.com) project for both authentication and data storage. Open the file in a browser (or host it anywhere static files are served) and it just works.

The page shows:

- An overall progress card — percentage complete, videos finished, days started/completed, and when progress was last updated.
- Four collapsible "Day" sections (Day 1–4), each listing its videos with a link to watch on YouTube.
- Per-video progress: a checkbox plus a dropdown to mark how much of that video you've actually finished — `0%`, `30%`, `50%`, `75%`, or `100%`.

## How progress tracking works

Each video's progress is stored as a percentage, keyed by an id like `d1-0`, `d1-1`, `d2-0`, etc. (day id + video index).

- Picking a value from the dropdown sets that video's percentage directly.
- Picking `100%` also auto-checks the checkbox, since checked = 100% under the hood — they're the same value, not two things to keep in sync.
- Checking the checkbox directly jumps that video to `100%`.
- Unchecking it drops the video back to `0%`.

Day-level and overall progress bars are the **average** of these percentages across all videos in scope, so partial progress actually moves the needle instead of only counting fully-finished videos. The "X / Y videos" count next to the overall bar still counts videos at a full 100%, so you can see both the fine-grained percentage and the number of videos truly done.

Older saved data (from before percentages existed) used plain `true`/`false` per video — the page still reads those correctly (`true` → 100%, `false`/missing → 0%) so nothing breaks on first load; going forward it writes numeric percentages.

## Public vs. owner mode

- **Everyone** who opens the page sees live progress — checkboxes and dropdowns are visible but disabled, so visitors can't change anything.
- **The owner** clicks "🔐 Owner login," signs in with an email/password registered in the Supabase project's Auth, and the page unlocks: checkboxes and dropdowns become editable, and a "↺ Reset all" button appears to clear all progress back to zero.

Access control isn't just hidden in the UI — it's enforced by Supabase Row Level Security (RLS) policies on the `progress` table, so even if someone bypassed the page's JavaScript, they couldn't write to the database without being authenticated as the owner.

## How data is stored

There's a single row in a Supabase table called `progress`:

| column | type | meaning |
|---|---|---|
| `id` | text | fixed value `"main"` — this app only ever reads/writes one row |
| `state` | jsonb | object of `{ "d1-0": 100, "d1-1": 30, ... }` — percentage per video |
| `last_update` | text | human-readable timestamp of the last edit |

On page load, the app fetches this row and renders progress from it. Whenever the owner changes a checkbox or dropdown, the app updates its in-memory `state` object, writes the whole row back to Supabase, and re-renders.

## Setup

1. Create a Supabase project.
2. Create the `progress` table as described above, with one seed row: `id = "main"`, `state = {}`, `last_update = null` (or any placeholder text).
3. Set up Row Level Security so that:
   - Anyone (anonymous) can `SELECT` the row.
   - Only an authenticated user (you) can `UPDATE` it.
4. Create yourself a user in Supabase Auth (email + password) — this is what you'll use to sign in as owner.
5. In `index.html`, replace `SUPABASE_URL` and `SUPABASE_PUBLISHABLE_KEY` near the top of the `<script>` block with your project's values (the public/anon key — never put a service-role/secret key in this file, since it's client-side code anyone can view).
6. Open `index.html` in a browser, or deploy it to any static host (GitHub Pages, Netlify, Vercel, S3, etc.).

## Customizing the course content

The days and videos are defined in the `DAYS` array near the top of the script — each day has an `id`, `name`, `desc`, and a `videos` array of `{ t: "title", url: "..." }` entries. Edit this array directly to add, remove, or reorder days/videos; the tracker will pick up the new structure automatically (existing saved progress is keyed by day id + index, so reordering videos within a day will shift which saved percentage applies to which video — add new videos at the end of a day's list to avoid this).
