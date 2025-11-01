# Contributing Guidelines

## Development Workflow

### Branch Strategy
This project follows a Git Flow branching model:

- **main**: Production-ready code
- **develop**: Integration branch for features
- **feature branches**: Individual feature development
- **hotfix branches**: Critical bug fixes

### Branch Naming Convention
- Feature: `feature/feature-name`
- Bug fix: `bugfix/issue-description`
- Hotfix: `hotfix/critical-fix`

### Commit Message Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Testing
- `chore`: Maintenance

**Examples:**
```
feat(submit): add form validation for request submission

fix(admin): resolve status update bug in admin panel

docs(readme): update installation instructions
```

## Development Setup

### Prerequisites
- Python 3.8+
- Git
- Virtual environment tool

### Local Development

1. **Fork and clone**:
   ```bash
   git clone https://github.com/your-username/Internal_Service_Request_Tracking-System.git
   cd Internal_Service_Request_Tracking-System
   ```

2. **Create feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Set up environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Run tests**:
   ```bash
   python -m pytest  # If tests are added later
   ```

5. **Run application**:
   ```bash
   python app.py
   ```

## Code Standards

### Python Style Guide
- Follow PEP 8 standards
- Use 4 spaces for indentation
- Maximum line length: 88 characters
- Use descriptive variable names

### Flask Best Practices
- Use blueprints for modular routing
- Implement proper error handling
- Validate all user inputs
- Use flash messages for user feedback

### Database Guidelines
- Use parameterized queries
- Implement proper connection handling
- Add database indexes for performance
- Use migrations for schema changes

### HTML/CSS Standards
- Use semantic HTML5
- Follow Bootstrap component guidelines
- Ensure responsive design
- Maintain accessibility standards

## Testing Guidelines

### Unit Tests
- Test all database functions
- Test form validation
- Test API integrations
- Mock external dependencies

### Integration Tests
- Test complete user workflows
- Test database operations
- Test external API calls

### Manual Testing Checklist
- [ ] Form submission works
- [ ] Admin panel displays requests
- [ ] Status updates function
- [ ] External API integration
- [ ] Responsive design
- [ ] Error handling

## Pull Request Process

### Before Submitting
1. **Update develop branch**:
   ```bash
   git checkout develop
   git pull origin develop
   ```

2. **Rebase your feature branch**:
   ```bash
   git checkout feature/your-feature
   git rebase develop
   ```

3. **Run tests and checks**:
   ```bash
   # Run any existing tests
   python -m pytest

   # Check code style
   flake8 .  # If configured
   ```

### Creating Pull Request

1. **Push your branch**:
   ```bash
   git push origin feature/your-feature
   ```

2. **Create PR on GitHub**:
   - Base branch: `develop`
   - Compare branch: `feature/your-feature`
   - Fill out PR template

3. **PR Description Template**:
   ```markdown
   ## Description
   Brief description of changes

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Breaking change
   - [ ] Documentation update

   ## Testing
   - [ ] Unit tests pass
   - [ ] Integration tests pass
   - [ ] Manual testing completed

   ## Screenshots (if applicable)
   Add screenshots of UI changes

   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Tests added/updated
   - [ ] Documentation updated
   - [ ] No breaking changes
   ```

### Code Review Process
1. **Automated checks**: CI/CD pipeline runs
2. **Peer review**: At least one reviewer required
3. **Approval**: Maintainers approve changes
4. **Merge**: Squash merge to develop branch

## Issue Reporting

### Bug Reports
**Template:**
```markdown
**Describe the bug**
Clear description of the issue

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What should happen

**Screenshots**
Add screenshots if applicable

**Environment:**
- OS: [e.g., Windows 10]
- Browser: [e.g., Chrome 91]
- Python version: [e.g., 3.9]
```

### Feature Requests
**Template:**
```markdown
**Is your feature request related to a problem?**
Description of the problem

**Describe the solution**
What you want to happen

**Describe alternatives**
Alternative solutions considered

**Additional context**
Add any other context or screenshots
```

## Security

### Reporting Security Issues
- Email security concerns to: security@example.com
- Do not create public GitHub issues for security vulnerabilities
- Allow 48 hours for initial response

### Security Best Practices
- Never commit sensitive data
- Use environment variables for secrets
- Validate all user inputs
- Keep dependencies updated
- Regular security audits

## Documentation

### Code Documentation
- Add docstrings to all functions
- Comment complex logic
- Update README for new features
- Maintain API documentation

### User Documentation
- Keep setup instructions current
- Document new features
- Update troubleshooting guides
- Maintain deployment guides

## Release Process

### Version Numbering
Follow Semantic Versioning (MAJOR.MINOR.PATCH)

### Release Checklist
- [ ] All tests pass
- [ ] Documentation updated
- [ ] Changelog updated
- [ ] Version number bumped
- [ ] Tag created and pushed
- [ ] Release notes published

## Community

### Code of Conduct
- Be respectful and inclusive
- Focus on constructive feedback
- Help newcomers learn
- Maintain professional communication

### Getting Help
- Check existing issues and documentation
- Use GitHub Discussions for questions
- Join community chat (if available)

## License
By contributing to this project, you agree that your contributions will be licensed under the MIT License.