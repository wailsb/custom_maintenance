# Odoo 18 Industrial Maintenance SI

![Odoo Version](https://img.shields.io/badge/Odoo-18.0-blue?style=flat-square&logo=odoo)
![License](https://img.shields.io/badge/License-LGPL--3-green.svg?style=flat-square)
![Status](https://img.shields.io/badge/Status-Production_Ready-success?style=flat-square)

An open-source, enterprise-grade Information System (SI) designed to track, manage, and execute industrial maintenance workflows. Built natively for **Odoo 18**, this module maps relational hardware assets to technical repair pipelines.

## System Architecture

This module introduces an isolated data schema mapping physical assets to transactional repair operations.

* **`maintenance.machine`**: The core asset entity, tracking location, technical specifications, and historical cost.
* **`maintenance.part`**: Child components strictly mapped to parent machines using cascaded relational integrity.
* **`maintenance.team`**: Extends Odoo's core `res.users` authentication model to handle specialized technical routing.
* **`maintenance.request`**: The transactional hub. Generates automated, sequential tickets (e.g., `REQ-0042`) triggered by machine failure.
* **`maintenance.operation`**: Granular execution logs linked to requests, detailing exact parts replaced and technicians assigned.

## Technical Highlights

* **Reactive Database Listeners:** Utilizes Odoo's `@api.depends` decorators to automatically calculate and inject assigned technical teams based on machine-level relationships.
* **Optimized Batch Processing:** Leverages `@api.model_create_multi` to intercept and process batch SQL inserts in memory, eliminating N+1 query inefficiencies during mass ticket creation.
* **Strict RBAC Security:** Implements granular Role-Based Access Control via `ir.model.access.csv`, restricting table modifications to authorized personnel.
* **Dynamic XML Views:** Abstracted UI layer utilizing Odoo 18's strict `<list>` and `<form>` view architectures, fully responsive for tablet and mobile deployment on the factory floor.

## Installation & Deployment

### Docker Environment (Recommended)
If running an isolated Odoo environment via Docker:

1. Clone this repository into your mounted Odoo `addons` directory:
   ```bash
   git clone [https://github.com/yourusername/odoo-custom-maintenance.git](https://github.com/yourusername/odoo-custom-maintenance.git) addons/custom_maintenance