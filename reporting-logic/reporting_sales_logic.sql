SELECT 
    -- 1. Eje Temporal
    d.date AS full_date,
    d.year,
    d.month_name,

    -- 2. Eje Geográfico y Demográfico
    u.country,
    u.city,
    u.gender,
    u.traffic_source,
    -- Regla de Negocio: Segmentación Etaria
    CASE 
        WHEN u.age < 18 THEN 'Gen Z (Menores)'
        WHEN u.age BETWEEN 18 AND 34 THEN 'Millennials'
        WHEN u.age BETWEEN 35 AND 50 THEN 'Gen X'
        ELSE 'Seniors'
    END AS customer_segment,

    -- 3. Eje de Producto (Consistente con dim_products)
    p.name AS product_name,
    p.category,
    p.brand,

    -- 4. Métricas Financieras y Reglas de Rentabilidad
    f.sale_price,
    f.product_cost,
    f.margin AS profit_amount,
    SAFE_DIVIDE(f.margin, f.sale_price) AS margin_rate,
    
    -- Regla de Negocio: Clasificación de Rentabilidad
    CASE 
        WHEN SAFE_DIVIDE(f.margin, f.sale_price) > 0.6 THEN 'Alta Rentabilidad'
        WHEN SAFE_DIVIDE(f.margin, f.sale_price) BETWEEN 0.3 AND 0.6 THEN 'Rentabilidad Media'
        ELSE 'Margen Crítico'
    END AS profit_tier,

    -- 5. Eje Operativo
    f.status AS order_status

FROM `ecommerce-data-pipeline-489322.core_ecommerce.fact_sales` f
JOIN `ecommerce-data-pipeline-489322.core_ecommerce.dim_users` u ON f.user_id = u.user_id
JOIN `ecommerce-data-pipeline-489322.core_ecommerce.dim_products` p ON f.product_id = p.product_id
JOIN `ecommerce-data-pipeline-489322.core_ecommerce.dim_date` d ON f.date_key = d.date_key;