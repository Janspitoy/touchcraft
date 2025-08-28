from django.db import models


class Service(models.Model):
    """Company services"""
    title = models.CharField(max_length=255, verbose_name="Service Title")
    description = models.TextField(verbose_name="Description")
    icon = models.CharField(max_length=100, verbose_name="Icon CSS Class (FontAwesome)")
    display_order = models.PositiveIntegerField(default=0, verbose_name="Display Order")

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title


class Project(models.Model):
    """Portfolio projects"""
    title = models.CharField(max_length=255, verbose_name="Project Title")
    description = models.TextField(verbose_name="Project Description")
    image = models.ImageField(upload_to="portfolio/", verbose_name="Image")
    link = models.URLField(blank=True, null=True, verbose_name="Project Link")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class Client(models.Model):
    """Client information"""
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone Number")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    """Client orders"""
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="orders", verbose_name="Client")
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",  # Добавлено для устранения конфликта
        verbose_name="Service"
    )
    project_description = models.TextField(verbose_name="Order Description")
    attached_files = models.FileField(upload_to="orders/files/", blank=True, null=True, verbose_name="Attached Files")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order #{self.id} — {self.client}"


class ContactMessage(models.Model):
    """Messages from contact form"""
    name = models.CharField(max_length=255, verbose_name="Sender Name")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone Number")
    message = models.TextField(verbose_name="Message")
    attached_file = models.FileField(upload_to="contacts/files/", blank=True, null=True, verbose_name="Attached File")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"Message from {self.name}"
