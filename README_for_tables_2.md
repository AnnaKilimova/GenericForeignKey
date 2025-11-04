### After creating a superuser without performing additional migrations

```bash
                    List of relations
 Schema |            Name            | Type  |    Owner    
--------+----------------------------+-------+-------------
 public | auth_group                 | table | kilimovaann
 public | auth_group_permissions     | table | kilimovaann
 public | auth_permission            | table | kilimovaann
 public | auth_user                  | table | kilimovaann
 public | auth_user_groups           | table | kilimovaann
 public | auth_user_user_permissions | table | kilimovaann
 public | django_admin_log           | table | kilimovaann
 public | django_content_type        | table | kilimovaann
 public | django_migrations          | table | kilimovaann
 public | django_session             | table | kilimovaann
(10 rows)
```

### auth_user
```bash
 id |        password         |   last_login   | is_superuser |  username   | first_name | last_name |   email   | is_staff | is_active |    date_joined          
----+-------------------------+----------------+--------------+-------------+------------+-----------+-----------+----------+-----------+---------------------
  1 | pbkdf2_sha256$1000000$p | 2025-11-02     |       t.     | kilimovaann |            |           | hk@hk.com |    t     |     t     | 2025-11-02
    | Y0wTg6WpO68JyIEuTAcD0$G | 17:16:30.278   |              |             |            |           |           |          |           | 17:15:24.955 
    | JptlMpp/gxXehrA3YPXgZPM | +0000          |              |             |            |           |           |          |           | +0000     
    | 4t+bRrtgPqiovjfg5fY=    |                |              |             |            |           |           |          |           | 
    |                         |                |              |             |            |           |           |          |           | 
(1 row)
```

### django_session
```bash
            session_key            |                     session_data                    |         expire_date 
-----------------------------------+-----------------------------------------------------+------------------------------
  r1nvq61ap7tb90l4zc6lrfb3znuqw991 | .eJxVjMsOwiAQRf-FtSHDS8Cl-34DGWCQqoGktCvjv2uTLn     | 2025-11-16 17:16:30.281 +0000
                                   | R7zzn3xQJuaw3boCXMmV2YYKffLWJ6UNtBvmO7dZ56          |
                                   | W5c58l3hBx186pme18P9O6g46rcmKQ0C2lKk8EVlpx          |
                                   | G09kY4lbJFrbyzkhJ4SGcRKWYDCsEZoKQVecneH9O6N2U:      |
                                   | 1vFbgs:F_hpqh0YZGze0oBXGPCVz1wwq20lUkm9g4csJ7f9i0E  |

(1 row)
```


