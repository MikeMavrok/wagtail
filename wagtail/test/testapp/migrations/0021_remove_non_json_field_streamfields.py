# Generated by Django 4.1.5 on 2023-01-31 15:35

from django.db import migrations
import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.test.testapp.models


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0020_genericsnippetnoindexpage_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="BlockCountsStreamModel",
        ),
        migrations.DeleteModel(
            name="MinMaxCountStreamModel",
        ),
        migrations.DeleteModel(
            name="StreamModel",
        ),
        migrations.AlterField(
            model_name="addedstreamfieldwithemptylistdefaultpage",
            name="body",
            field=wagtail.fields.StreamField(
                [("title", wagtail.blocks.CharBlock())], default=[], use_json_field=True
            ),
        ),
        migrations.AlterField(
            model_name="addedstreamfieldwithemptystringdefaultpage",
            name="body",
            field=wagtail.fields.StreamField(
                [("title", wagtail.blocks.CharBlock())], default="", use_json_field=True
            ),
        ),
        migrations.AlterField(
            model_name="addedstreamfieldwithoutdefaultpage",
            name="body",
            field=wagtail.fields.StreamField(
                [("title", wagtail.blocks.CharBlock())], use_json_field=True
            ),
        ),
        migrations.AlterField(
            model_name="customrichblockfieldpage",
            name="body",
            field=wagtail.fields.StreamField(
                [("rich_text", wagtail.blocks.RichTextBlock(editor="custom"))],
                use_json_field=True,
            ),
        ),
        migrations.AlterField(
            model_name="deadlystreampage",
            name="body",
            field=wagtail.fields.StreamField(
                [("title", wagtail.test.testapp.models.DeadlyCharBlock())],
                use_json_field=True,
            ),
        ),
        migrations.AlterField(
            model_name="defaultrichblockfieldpage",
            name="body",
            field=wagtail.fields.StreamField(
                [("rich_text", wagtail.blocks.RichTextBlock())], use_json_field=True
            ),
        ),
        migrations.AlterField(
            model_name="defaultstreampage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("text", wagtail.blocks.CharBlock()),
                    ("rich_text", wagtail.blocks.RichTextBlock()),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                ],
                default="",
                use_json_field=True,
            ),
        ),
        migrations.AlterField(
            model_name="inlinestreampagesection",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("text", wagtail.blocks.CharBlock()),
                    ("rich_text", wagtail.blocks.RichTextBlock()),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                ],
                use_json_field=True,
            ),
        ),
        migrations.AlterField(
            model_name="streampage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("text", wagtail.blocks.CharBlock()),
                    ("rich_text", wagtail.blocks.RichTextBlock()),
                    ("image", wagtail.test.testapp.models.ExtendedImageChooserBlock()),
                    (
                        "product",
                        wagtail.blocks.StructBlock(
                            [
                                ("name", wagtail.blocks.CharBlock()),
                                ("price", wagtail.blocks.CharBlock()),
                            ]
                        ),
                    ),
                    ("raw_html", wagtail.blocks.RawHTMLBlock()),
                    (
                        "books",
                        wagtail.blocks.StreamBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("author", wagtail.blocks.CharBlock()),
                            ]
                        ),
                    ),
                    (
                        "title_list",
                        wagtail.blocks.ListBlock(wagtail.blocks.CharBlock()),
                    ),
                ],
                use_json_field=True,
            ),
        ),
        migrations.AlterField(
            model_name="tableblockstreampage",
            name="table",
            field=wagtail.fields.StreamField(
                [("table", wagtail.contrib.table_block.blocks.TableBlock())],
                use_json_field=True,
            ),
        ),
    ]