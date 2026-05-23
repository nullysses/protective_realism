# Push instructions

The ChatGPT GitHub connector available in this session can write files to an existing repository, but it does not expose a top-level repository creation action. Create the empty repository first, then push this scaffold.

Using GitHub CLI:

```bash
gh repo create nullysses/protective_realism --public --source=. --remote=origin --push
```

Or, if you prefer private first:

```bash
gh repo create nullysses/protective_realism --private --source=. --remote=origin --push
```

Using git after creating the empty repo in GitHub UI:

```bash
git init
git add .
git commit -m "Initial Protective Realism eval scaffold"
git branch -M main
git remote add origin git@github.com:nullysses/protective_realism.git
git push -u origin main
```
