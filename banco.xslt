<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<banco>
    <clientes>
        <xsl:for-each select="banco/clientes/cliente">
            <xsl:variable name="cliente_key" select="@id" />
            <cliente>
                <cliente_id><xsl:value-of select="@id"/></cliente_id>
                <nombre><xsl:value-of select="nombre"/></nombre>
                <direccion><xsl:value-of select="direccion"/></direccion>
                <dni><xsl:value-of select="dni"/></dni>
                <cuentas>
                  <xsl:for-each select="/banco/clientes_cuentas/cliente_cuenta[@c_id=$cliente_key]">
                    <xsl:variable name="cuenta_key" select="@cu_id" />
                    <xsl:for-each select="/banco/cuentas/cuentas_corrientes/cuenta_corriente[@id=$cuenta_key]">
                      <cuenta>
                          <cuenta_id><xsl:value-of select="@id"/></cuenta_id>
                          <tipo>cuenta_corriente</tipo>
                          <balance><xsl:value-of select="balance"/></balance>
                          <interes><xsl:value-of select="interes"/></interes>
                      </cuenta>
                    </xsl:for-each>
                    <xsl:for-each select="/banco/cuentas/caja_ahorros/caja_ahorro[@id=$cuenta_key]">
                      <cuenta>
                          <cuenta_id><xsl:value-of select="@id"/></cuenta_id>
                          <tipo>caja_ahorro</tipo>
                          <balance><xsl:value-of select="balance"/></balance>
                          <interes><xsl:value-of select="interes"/></interes>
                      </cuenta>
                    </xsl:for-each>
                  </xsl:for-each>
                </cuentas>
            </cliente>
        </xsl:for-each>
    </clientes>
</banco>
</xsl:template>
</xsl:stylesheet>
